%global __brp_check_rpaths %{nil}
%global packname  rollinglda
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Construct Consistent Time Series from Textual Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-checkmate >= 1.8.5
BuildRequires:    R-CRAN-data.table >= 1.11.2
BuildRequires:    R-CRAN-ldaPrototype >= 0.3.0
BuildRequires:    R-CRAN-tosca >= 0.2.0
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-checkmate >= 1.8.5
Requires:         R-CRAN-data.table >= 1.11.2
Requires:         R-CRAN-ldaPrototype >= 0.3.0
Requires:         R-CRAN-tosca >= 0.2.0
Requires:         R-CRAN-lubridate 
Requires:         R-stats 
Requires:         R-utils 

%description
A rolling version of the Latent Dirichlet Allocation, see Rieger et al.
(2021)
<https://www.statistik.tu-dortmund.de/fileadmin/user_upload/Lehrstuehle/IWuS/Forschung/rollinglda.pdf>.
By a sequential approach, it enables the construction of LDA-based time
series of topics that are consistent with previous states of LDA models.
After an initial modeling, updates can be computed efficiently, allowing
for real-time monitoring and detection of events or structural breaks.

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
