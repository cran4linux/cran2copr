%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  panelSUR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Two-Way Error Component SUR Systems Estimation on Unbalanced Panel Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-formula.tools 
BuildRequires:    R-CRAN-plm 
BuildRequires:    R-CRAN-matlib 
BuildRequires:    R-CRAN-fastmatrix 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-formula.tools 
Requires:         R-CRAN-plm 
Requires:         R-CRAN-matlib 
Requires:         R-CRAN-fastmatrix 

%description
Generalized Least Squares (GLS) estimation of Seemingly Unrelated
Regression (SUR) systems on unbalanced panel in the one/two-way cases also
taking into account the possibility of cross equation restrictions.
Methodological details can be found in Biørn (2004)
<doi:10.1016/j.jeconom.2003.10.023> and Platoni, Sckokai, Moro (2012)
<doi:10.1080/07474938.2011.607098>.

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
