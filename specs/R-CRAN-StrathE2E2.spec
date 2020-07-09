%global packname  StrathE2E2
%global packver   3.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.0
Release:          1%{?dist}
Summary:          End-to-End Marine Food Web Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-NetIndices 
Requires:         R-CRAN-deSolve 
Requires:         R-methods 
Requires:         R-CRAN-NetIndices 

%description
A dynamic model of the big-picture, whole ecosystem effects of
hydrodynamics, temperature, nutrients, and fishing on continental shelf
marine food webs. The package has been developed from a prototype
described in: Heath, M.R. (2012) <doi:10.1016/j.pocean.2012.03.004>
Ecosystem limits to food web fluxes and fisheries yields in the North Sea
simulated with an end-to-end food web model. Progress in Oceanography
(Special issue: End-to-end modelling: Towards Comparative Analysis of
Marine Ecosystem Organisation) 102, 42-66.

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
