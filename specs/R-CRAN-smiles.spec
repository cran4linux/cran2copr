%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  smiles
%global packver   0.1-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Sequential Method in Leading Evidence Synthesis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-meta 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-boot 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-meta 
Requires:         R-stats 
Requires:         R-utils 

%description
Trial sequential analysis emerges as an important method in data synthesis
realm. It is necessary to integrate pooling methods and sequential
analysis coherently, as discussed in the Chapter by Thomas, J., Askie,
L.M., Berlin, J.A., Elliott, J.H., Ghersi, D., Simmonds, M., Takwoingi,
Y., Tierney, J.F. and Higgins, J.P. (2019). "Prospective approaches to
accumulating evidence". In Cochrane Handbook for Systematic Reviews of
Interventions (eds J.P.T. Higgins, J. Thomas, J. Chandler, M. Cumpston, T.
Li, M.J. Page and V.A. Welch). <doi:10.1002/9781119536604.ch22>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
