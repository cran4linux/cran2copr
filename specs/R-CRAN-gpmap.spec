%global packname  gpmap
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Analysing and plotting genotype-phenotype maps

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-isotone 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-isotone 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-foreach 

%description
This package contains tools for studying genotype-phenotype (GP) maps for
bi-allelic loci underlying quantitative phenotypes. The 0.1 version is
released in connection with the publication of Gjuvsland et al. (2003) and
implements basic line plots and the monotonicity measures for GP maps
presented in the paper. Reference: Gjuvsland AB, Wang Y, Plahte E and
Omholt SW (2013) Monotonicity is a key feature of genotype-phenotype maps.
Front. Genet. 4:216. doi: 10.3389/fgene.2013.00216
[href{http://www.frontiersin.org/Journal/10.3389/fgene.2013.00216/full}{link}]

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
