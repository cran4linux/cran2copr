%global packname  xtreg2way
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Feasible Estimation of the Two-Way Fixed Effect Model

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
Requires:         R-CRAN-pracma 
Requires:         R-Matrix 
Requires:         R-stats 
Requires:         R-MASS 

%description
Implemented is an algorithm to estimate the two-way fixed effect linear
model. The coefficients of interest are computed using the residuals from
the projection of all variables on the two sets of fixed effects. Our
algorithm has three desirable features. First, it manages memory and
computational resources efficiently which speeds up the computation of the
estimates. Second, it allows the researcher to estimate multiple
specifications using the same set of fixed effects at a very low
computational cost. Third, the asymptotic variance of the parameters of
interest can be consistently estimated using standard routines on the
residualized data. Somaini P., Wolak F. A. (2016)
<doi:10.1515/jem-2014-0008> Arellano, M. (1987)
<https://ideas.repec.org/a/bla/obuest/v49y1987i4p431-34.html>.

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
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
