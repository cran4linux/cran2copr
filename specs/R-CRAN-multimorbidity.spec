%global __brp_check_rpaths %{nil}
%global packname  multimorbidity
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Harmonizing Various Comorbidity, Multimorbidity, and Frailty Measures

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-sqldf 
BuildRequires:    R-stats 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-sqldf 
Requires:         R-stats 

%description
Identifying comorbidities, frailty, and multimorbidity in claims and
administrative data is often a duplicative process. The functions
contained in this package are meant to first prepare the data to a format
acceptable by all other packages, then provide a uniform and simple
approach to generate comorbidity and multimorbidity metrics based on these
claims data. The package is ever evolving to include new metrics, and is
always looking for new measures to include. The citations used in this
package include the following publications: Anne Elixhauser, Claudia
Steiner, D. Robert Harris, Rosanna M. Coffey (1998)
<doi:10.1097/00005650-199801000-00004>, Brian J Moore, Susan White,
Raynard Washington, et al. (2017) <doi:10.1097/MLR.0000000000000735>, Mary
E. Charlson, Peter Pompei, Kathy L. Ales, C. Ronald MacKenzie (1987)
<doi:10.1016/0021-9681(87)90171-8>, Richard A. Deyo, Daniel C. Cherkin,
Marcia A. Ciol (1992) <doi:10.1016/0895-4356(92)90133-8>, Hude Quan,
Vijaya Sundararajan, Patricia Halfon, et al. (2005)
<doi:10.1097/01.mlr.0000182534.19832.83>, Dae Hyun Kim, Sebastian
Schneeweiss, Robert J Glynn, et al. (2018) <doi:10.1093/gerona/glx229>,
Melissa Y Wei, David Ratz, Kenneth J Mukamal (2020)
<doi:10.1111/jgs.16310>, Kathryn Nicholson, Amanda L. Terry, Martin
Fortin, et al. (2015) <doi:10.15256/joc.2015.5.61>, Martin Fortin, José
Almirall, and Kathryn Nicholson (2017)<doi:10.15256/joc.2017.7.122>.

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
