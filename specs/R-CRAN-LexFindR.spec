%global __brp_check_rpaths %{nil}
%global packname  LexFindR
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Find Related Items and Lexical Dimensions in a Lexicon

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch

%description
Implements code to identify lexical competitors in a given list of words.
We include many of the standard competitor types used in spoken word
recognition research, such as functions to find cohorts, neighbors, and
rhymes, amongst many others. The package includes documentation for using
a variety of lexicon files, including those with form codes made up of
multiple letters (i.e., phoneme codes) and also basic orthographies.
Importantly, the code makes use of multiple CPU cores and vectorization
when possible, making it extremely fast and able to handle large lexicons.
Additionally, the package contains documentation for users to easily write
new functions, allowing researchers to examine other relationships within
a lexicon. Preprint: <https://psyarxiv.com/8dyru/>. Open access:
<https://link.springer.com/epdf/10.3758/s13428-021-01667-6?sharing_token=9WlO9soCc9y0uSuwWSUYfJAH0g46feNdnc402WrhzyrdKcK8uzZx_hDEtgbYzn3gvxdG5Cuj0j0cC4lVMFBqYCGTQmE2blN2Gwo74LJ8ro1pEOAYDRFy6Lhf1nc719vD-zU7GDvKOQxDAwPbrisvPBeXSIu0NkqXF7Jx3IuUwIs%%3D>.
Citation: Li, Z., Crinnion, A.M. & Magnuson, J.S. (2021).
<doi:10.3758/s13428-021-01667-6>.

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
