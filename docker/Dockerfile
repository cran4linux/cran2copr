ARG VERSION=rawhide
FROM registry.fedoraproject.org/fedora:$VERSION

LABEL org.label-schema.license="GPL-2.0" \
      org.label-schema.vcs-url="https://github.com/Enchufa2/cran2copr" \
      maintainer="Iñaki Ucar <iucar@fedoraproject.org>"

RUN echo "install_weak_deps=False" >> /etc/dnf/dnf.conf \
    && dnf -y upgrade && dnf -y install R && dnf -y clean all

RUN dnf -y install 'dnf-command(copr)' \
    && dnf -y copr enable iucar/cran \
    && sed -ie '/nodocs/d' /etc/dnf/dnf.conf \
    && dnf -y install sudo R-CoprManager && dnf -y clean all \
    && echo "options(CoprManager.sudo=TRUE)" > \
        /usr/lib64/R/etc/Rprofile.site.d/51-CoprManager-sudo.site \
    && echo "options(repos='https://cloud.r-project.org')" > \
        /usr/lib64/R/etc/Rprofile.site.d/00-repos.site

RUN useradd -m docker \
    && echo "docker ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/docker-user \
    && chmod 0440 /etc/sudoers.d/docker-user \
    && mkdir -p /usr/local/lib/R/site-library \
    && chown 1000:1000 /usr/local/lib/R/site-library

RUN dnf -y install R-littler-examples R-CRAN-remotes && dnf -y clean all \
    && ln -s /usr/lib64/R/library/littler/examples/install.r \
        /usr/local/bin/install.r \
    && ln -s /usr/lib64/R/library/littler/examples/install2.r \
        /usr/local/bin/install2.r \
    && ln -s /usr/lib64/R/library/littler/examples/installGithub.r \
        /usr/local/bin/installGithub.r \
    && ln -s /usr/lib64/R/library/littler/examples/testInstalled.r \
        /usr/local/bin/testInstalled.r

CMD ["bash"]
