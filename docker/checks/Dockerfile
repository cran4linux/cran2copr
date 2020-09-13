ARG TAG=rawhide
FROM fedora:${TAG}

MAINTAINER "Iñaki Úcar" iucar@fedoraproject.org

RUN dnf install 'dnf-command(copr)' -y
RUN dnf copr enable iucar/cran -y

ENTRYPOINT ["dnf", "repoclosure", "--check=copr:copr.fedorainfracloud.org:iucar:cran"]
