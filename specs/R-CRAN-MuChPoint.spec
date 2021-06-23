%global __brp_check_rpaths %{nil}
%global packname  MuChPoint
%global packver   0.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.1
Release:          3%{?dist}%{?buildtag}
Summary:          Multiple Change Point

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-capushe 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-Matrix 
Requires:         R-CRAN-capushe 
Requires:         R-CRAN-shiny 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 

%description
Nonparametric approach to estimate the location of block boundaries
(change-points) of non-overlapping blocks in a random symmetric matrix
which consists of random variables whose distribution changes from block
to block. BRAULT Vincent, OUADAH Sarah, SANSONNET Laure and LEVY-LEDUC
Celine (2017) <doi:10.1016/j.jmva.2017.12.005>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
