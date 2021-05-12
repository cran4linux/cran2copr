%global packname  bumblebee
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Quantify Disease Transmission Within and Between Population Groups

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-Hmisc >= 4.4.2
BuildRequires:    R-CRAN-gtools >= 3.8.2
BuildRequires:    R-CRAN-rmarkdown >= 2.6
BuildRequires:    R-CRAN-magrittr >= 2.0.1
BuildRequires:    R-CRAN-dplyr >= 1.0.2
Requires:         R-CRAN-Hmisc >= 4.4.2
Requires:         R-CRAN-gtools >= 3.8.2
Requires:         R-CRAN-rmarkdown >= 2.6
Requires:         R-CRAN-magrittr >= 2.0.1
Requires:         R-CRAN-dplyr >= 1.0.2

%description
A simple tool to quantify the amount of transmission of an infectious
disease of interest occurring within and between population groups.
'bumblebee' uses counts of observed directed transmission pairs,
identified phylogenetically from deep-sequence data or from
epidemiological contacts, to quantify transmission flows within and
between population groups accounting for sampling heterogeneity.
Population groups might include: geographical areas (e.g. communities,
regions), demographic groups (e.g. age, gender) or arms of a randomized
clinical trial. See the 'bumblebee' website for statistical theory,
documentation and examples <https://magosil86.github.io/bumblebee/>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
