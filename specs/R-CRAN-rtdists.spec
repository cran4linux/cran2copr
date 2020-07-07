%global packname  rtdists
%global packver   0.11-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.11.2
Release:          3%{?dist}
Summary:          Response Time Distributions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-gsl 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-evd 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-gsl 
Requires:         R-stats 
Requires:         R-CRAN-Rcpp 

%description
Provides response time distributions (density/PDF, distribution
function/CDF, quantile function, and random generation): (a) Ratcliff
diffusion model (Ratcliff & McKoon, 2008,
<doi:10.1162/neco.2008.12-06-420>) based on C code by Andreas and Jochen
Voss and (b) linear ballistic accumulator (LBA; Brown & Heathcote, 2008,
<doi:10.1016/j.cogpsych.2007.12.002>) with different distributions
underlying the drift rate.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
