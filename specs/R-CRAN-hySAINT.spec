%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hySAINT
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Hybrid Genetic and Simulated Annealing Algorithm for High Dimensional Linear Models with Interaction Effects

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-energy 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-selectiveInference 
BuildRequires:    R-CRAN-VariableScreening 
BuildRequires:    R-CRAN-SIS 
Requires:         R-utils 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-energy 
Requires:         R-CRAN-pracma 
Requires:         R-stats 
Requires:         R-CRAN-selectiveInference 
Requires:         R-CRAN-VariableScreening 
Requires:         R-CRAN-SIS 

%description
We provide a stage-wise selection method using genetic algorithms,
designed to efficiently identify main and two-way interactions within
high-dimensional linear regression models. Additionally, it implements
simulated annealing algorithm during the mutation process. The relevant
paper can be found at: Ye, C.,and Yang,Y. (2019)
<doi:10.1109/TIT.2019.2913417>.

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
