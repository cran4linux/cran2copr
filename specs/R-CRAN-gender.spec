%global __brp_check_rpaths %{nil}
%global packname  gender
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Predict Gender from Names Using Historical Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-remotes >= 2.2.0
BuildRequires:    R-CRAN-jsonlite >= 1.6.1
BuildRequires:    R-CRAN-httr >= 1.4.1
BuildRequires:    R-CRAN-dplyr >= 0.8.5
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-remotes >= 2.2.0
Requires:         R-CRAN-jsonlite >= 1.6.1
Requires:         R-CRAN-httr >= 1.4.1
Requires:         R-CRAN-dplyr >= 0.8.5
Requires:         R-utils 
Requires:         R-stats 

%description
Infers state-recorded gender categories from first names and dates of
birth using historical datasets. By using these datasets instead of lists
of male and female names, this package is able to more accurately infer
the gender of a name, and it is able to report the probability that a name
was male or female. GUIDELINES: This method must be used cautiously and
responsibly. Please be sure to see the guidelines and warnings about usage
in the 'README' or the package documentation. See Blevins and Mullen
(2015) <http://www.digitalhumanities.org/dhq/vol/9/3/000223/000223.html>.

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
