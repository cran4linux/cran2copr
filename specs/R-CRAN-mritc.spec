%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mritc
%global packver   0.5-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.3
Release:          1%{?dist}%{?buildtag}
Summary:          MRI Tissue Classification

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildRequires:    R-CRAN-misc3d >= 0.8.1
BuildRequires:    R-CRAN-oro.nifti >= 0.4.0
BuildRequires:    R-CRAN-lattice >= 0.18.8
BuildRequires:    R-methods 
Requires:         R-CRAN-misc3d >= 0.8.1
Requires:         R-CRAN-oro.nifti >= 0.4.0
Requires:         R-CRAN-lattice >= 0.18.8
Requires:         R-methods 

%description
Implements various methods for tissue classification in magnetic resonance
(MR) images of the brain, including normal mixture models and hidden
Markov normal mixture models, as outlined in Feng & Tierney (2011)
<doi:10.18637/jss.v044.i07>. These methods allow a structural MR image to
be classified into gray matter, white matter and cerebrospinal fluid
tissue types.

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
