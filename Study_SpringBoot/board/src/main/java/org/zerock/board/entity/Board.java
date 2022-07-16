package org.zerock.board.entity;

import lombok.*;

import javax.persistence.*;

@Entity
@Builder
@AllArgsConstructor
@NoArgsConstructor
@Getter
@ToString(exclude = "writer")
public class Board extends BaseEntity{
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long bto;

    private String title;

    private String content;

    @ManyToOne (fetch = FetchType.LAZY) //명시적으로 Lazy 로딩 지정
    private Member writer; //연관관계 지정

    public void changeTitle(String title){
        this.title = title;
    }

    public void changeContent(String Content){
        this.content = content;
    }
}
