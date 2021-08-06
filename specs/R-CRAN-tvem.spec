%global __brp_check_rpaths %{nil}
%global packname  tvem
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Time-Varying Effect Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mgcv 
Requires:         R-CRAN-mgcv 

%description
Fits time-varying effect models (TVEM). These are a kind of application of
varying-coefficient models in the context of longitudinal data, allowing
the strength of linear, logistic, or Poisson regression relationships to
change over time.  These models are described further in Tan, Shiyko, Li,
Li & Dierker (2012) <doi:10.1037/a0025814>.  We thank Kaylee Litson,
Patricia Berglund, and Yajnaseni Chakraborti for their valuable help with
testing the package and documentation. The development of this package was
part of a research project supported by National Institutes of Health
grants P50 DA039838 from the National Institute of Drug Abuse and 1R01
CA229542-01 from the National Cancer Institute and the NIH Office of
Behavioral and Social Science Research. Content is solely the
responsibility of the authors and does not necessarily represent the
official views of the funding institutions mentioned above. This software
is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
details.

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
