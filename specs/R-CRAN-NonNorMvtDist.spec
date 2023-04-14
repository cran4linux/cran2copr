%global __brp_check_rpaths %{nil}
%global packname  NonNorMvtDist
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Multivariate Lomax (Pareto Type II) and Its RelatedDistributions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-cubature 
Requires:         R-stats 
Requires:         R-CRAN-cubature 

%description
Implements calculation of probability density function, cumulative
distribution function, equicoordinate quantile function and survival
function, and random numbers generation for the following multivariate
distributions: Lomax (Pareto Type II), generalized Lomax, Mardia’s Pareto
of Type I, Logistic, Burr, Cook-Johnson’s uniform, F and Inverted Beta.
See Tapan Nayak (1987) <doi:10.2307/3214068>.

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
%{rlibdir}/%{packname}
