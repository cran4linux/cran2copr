%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dnafractal
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Generates a Fractal Image of a DNA Sequence

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-DescTools 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-DescTools 

%description
The function takes a DNA sequence, a start point, an end point in the
sequence, dot size and dot color and draws a fractal image of the
sequence. The fractal starts in the center of the canvas. The image is
drawn by moving base by base along the sequence and dropping a midpoint
between the actual point and the corner designated by the actual base. For
more details see Jeffrey (1990) <doi:10.1093/nar/18.8.2163>, Hill,
Schisler, and Singh (1992) <doi:10.1007/BF00178602>, and Löchel and Heider
(2021) <doi:10.1016/j.csbj.2021.11.008>.

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
