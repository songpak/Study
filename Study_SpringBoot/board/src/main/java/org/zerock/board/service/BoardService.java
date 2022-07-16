package org.zerock.board.service;

import org.zerock.board.dto.BoardDTO;
import org.zerock.board.dto.PageRequestDTO;
import org.zerock.board.dto.PageResultDTO;
import org.zerock.board.entity.Board;
import org.zerock.board.entity.Member;

public interface BoardService {
    Long register(BoardDTO dto);

    PageResultDTO<BoardDTO,Object[]> getList(PageRequestDTO pageRequestDTO); //목록 처리

    void removeWithReplies(Long bto); //삭제 기능

    void modify(BoardDTO boardDTO);

    BoardDTO get(Long bto);

    default Board dtoToEntity(BoardDTO dto){
        Member member = Member.builder().email(dto.getWriterEmail()).build();

        Board board = Board.builder()
                .bto(dto.getBto())
                .title(dto.getTitle())
                .content(dto.getContent())
                .writer(member)
                .build();

        return board;
    }

    //BoardService 인터페이스에 추가하는 entityToDTO()
    default BoardDTO entityToDTO(Board board,Member member, Long replyCount){
        BoardDTO boardDTO = BoardDTO.builder()
                .bto(board.getBto())
                .title(board.getTitle())
                .content(board.getContent())
                .regDate(board.getRegDate())
                .modDate(board.getModDate())
                .writerEmail(member.getEmail())
                .writerName(member.getName())
                .replyCount(replyCount.intValue()) //long으로 나오므로 int로 처리하도록
                .build();

        return boardDTO;
    }
}
