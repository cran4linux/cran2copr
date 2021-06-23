%global __brp_check_rpaths %{nil}
%global packname  ExtremalDep
%global packver   0.0.3-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3.3
Release:          2%{?dist}%{?buildtag}
Summary:          Extremal Dependence Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-CompRandFld 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-fda 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-evd 
Requires:         R-CRAN-sn 
Requires:         R-CRAN-CompRandFld 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-fda 

%description
A set of procedures for modelling parametrically and non-parametrically
the dependence structure of multivariate extreme-values is provided. The
statistical inference is performed with non-parametric estimators,
likelihood-based estimators and Bayesian techniques. Adapts the
methodologies derived in Beranger et al. (2019) <arxiv:1904.08251>,
Beranger et al. (2017) <doi:10.1111/sjos.12240>, Beranger and Padoan
(2015) <arxiv:1508.05561>, Marcon et al. (2017) <doi:10.1002/sta4.145>,
Marcon et al. (2017) <doi:10.1016/j.jspi.2016.10.004> and Marcon et al.
(2016) <doi:10.1214/16-EJS1162>. It also refers to the works of Bortot
(2010)
<https://pdfs.semanticscholar.org/b0dc/1cb608d35bf515c76e39aacc14b4de82e281.pdf>,
Padoan (2011) <doi:10.1016/j.jmva.2011.01.014>, Cooley et al. (2010)
<doi:10.1016/j.jmva.2010.04.007>, Husler and Reiss (1989)
<doi:10.1016/0167-7152(89)90106-5>, Engelke et al. (2015)
<doi:10.1111/rssb.12074>, Coles and Tawn (1991)
<doi:10.1111/j.2517-6161.1991.tb01830.x>, Nikoloulopoulos et al. (2011)
<doi:10.1007/s10687-008-0072-4>, Opitz (2013)
<doi:10.1016/j.jmva.2013.08.008>, Tawn (1990) <doi:10.2307/2336802>,
Azzalini (1985) <https://www.jstor.org/stable/pdf/4615982.pdf>, Azzalini
and Capitanio (2014) <doi:10.1017/CBO9781139248891>, Azzalini (2003)
<doi:10.1111/1467-9469.00322>, Azzalini and Capitanio (1999)
<doi:10.1111/1467-9868.00194>, Azzalini and Dalla Valle (1996)
<doi:10.1093/biomet/83.4.715>, Einmahl et al. (2013)
<doi:10.1007/s10687-012-0156-z>, Naveau et al (2009)
<doi:10.1093/biomet/asp001> and Heffernan and Tawn (2004)
<doi:10.1111/j.1467-9868.2004.02050.x>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
