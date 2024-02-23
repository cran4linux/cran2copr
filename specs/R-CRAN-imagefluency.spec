%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  imagefluency
%global packver   0.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Image Statistics Based on Processing Fluency

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-readbitmap 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-OpenImageR 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-readbitmap 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-OpenImageR 

%description
Get image statistics based on processing fluency theory. The functions
provide scores for several basic aesthetic principles that facilitate
fluent cognitive processing of images: contrast, complexity / simplicity,
self-similarity, symmetry, and typicality. See Mayer & Landwehr (2018)
<doi:10.1037/aca0000187> and Mayer & Landwehr (2018)
<doi:10.31219/osf.io/gtbhw> for the theoretical background of the methods.

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
