%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SK4FGA
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Scott-Knott for Forensic Glass Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-Rcpp 

%description
In forensics, it is common and effective practice to analyse glass
fragments from the scene and suspects to gain evidence of placing a
suspect at the crime scene. This kind of analysis involves comparing the
physical and chemical attributes of glass fragments that exist on both the
person and at the crime scene, and assessing the significance in a
likeness that they share. The package implements the Scott-Knott
Modification 2 algorithm (SKM2) (Christopher M. Triggs and James M. Curran
and John S. Buckleton and Kevan A.J. Walsh (1997)
<doi:10.1016/S0379-0738(96)02037-3> "The grouping problem in forensic
glass analysis: a divisive approach", Forensic Science International,
85(1), 1--14) for small sample glass fragment analysis using the
refractive index (ri) of a set of glass samples. It also includes an
experimental multivariate analog to the Scott-Knott algorithm for similar
analysis on glass samples with multiple chemical concentration variables
and multiple samples of the same item; testing against the Hotellings T^2
distribution (J.M. Curran and C.M. Triggs and J.R. Almirall and J.S.
Buckleton and K.A.J. Walsh (1997) <doi:10.1016/S1355-0306(97)72197-X> "The
interpretation of elemental composition measurements from forensic glass
evidence", Science & Justice, 37(4), 241--244).

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
