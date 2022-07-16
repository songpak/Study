package org.zerock.board.repository;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.zerock.board.entity.Board;
import org.zerock.board.repository.search.SearchBoardRepository;

import java.util.List;

public interface BoardRepository extends JpaRepository<Board,Long>, SearchBoardRepository {
    //한개의 로우(Object) 내에 Object[]로 나옴
    @Query("select b,w from Board b left join b.writer w where b.bto =:bto")
    Object getBoardWithWriter(@Param("bto") Long bto);

    @Query("SELECT b,r FROM Board b LEFT JOIN Reply r ON r.board = b WHERE b.bto = :bto")
    List<Object[]> getBoardWithReply(@Param("bto") Long bto);

    @Query(value="SELECT b,w, count(r)" +
            "FROM Board b " +
            "LEFT JOIN b.writer w " +
            "LEFT JOIN Reply r ON r.board = b " +
            "GROUP BY b",
            countQuery = "SELECT count(b) FROM Board b")
    Page<Object[]> getBoardWithReplyCount(Pageable pageable); //목록 화면에 필요한 데이터

    @Query("SELECT b, w, count(r) " +
            "FROM Board b LEFT JOIN b.writer w " +
            "LEFT OUTER JOIN Reply r ON r.board = b " +
            "WHERE b.bto = :bto")
    Object getBoardByBto(@Param("bto") Long bto);
}
