%global __brp_check_rpaths %{nil}
%global packname  sylcount
%global packver   0.2-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Syllable Counting and Readability Measurements

License:          BSD 2-clause License + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0

%description
An English language syllable counter, plus readability score measure-er.
For readability, we support 'Flesch' Reading Ease and 'Flesch-Kincaid'
Grade Level ('Kincaid' 'et al'. 1975)
<https://stars.library.ucf.edu/cgi/viewcontent.cgi?article=1055&context=istlibrary>,
Automated Readability Index ('Senter' and Smith 1967)
<https://apps.dtic.mil/sti/citations/AD0667273>, Simple Measure of
Gobbledygook (McLaughlin 1969)
<https://www.semanticscholar.org/paper/SMOG-Grading-A-New-Readability-Formula.-Laughlin/5fccb74c14769762b3de010c5e8a1a7ce700d17a>,
and 'Coleman-Liau' (Coleman and 'Liau' 1975) <doi:10.1037/h0076540>. The
package has been carefully optimized and should be very efficient, both in
terms of run time performance and memory consumption. The main methods are
'vectorized' by document, and scores for multiple documents are computed
in parallel via 'OpenMP'.

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
