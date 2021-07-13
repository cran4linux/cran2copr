%global __brp_check_rpaths %{nil}
%global packname  polypharmacy
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate Several Polypharmacy Indicators

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-itertools 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-itertools 
Requires:         R-CRAN-lubridate 
Requires:         R-parallel 
Requires:         R-CRAN-stringr 

%description
Analyse prescription drug deliveries to calculate several indicators of
polypharmacy corresponding to the various definitions found in the
literature. Bjerrum, L., Rosholm, J. U., Hallas, J., & Kragstrup, J.
(1997) <doi:10.1007/s002280050329>. Chan, D.-C., Hao, Y.-T., & Wu, S.-C.
(2009a) <doi:10.1002/pds.1712>. Fincke, B. G., Snyder, K., Cantillon, C.,
Gaehde, S., Standring, P., Fiore, L., ... Gagnon, D.R. (2005)
<doi:10.1002/pds.966>. Hovstadius, B., Astrand, B., & Petersson, G. (2009)
<doi:10.1186/1472-6904-9-11>. Hovstadius, B., Astrand, B., & Petersson, G.
(2010) <doi:10.1002/pds.1921>. Kennerfalk, A., Ruigómez, A., Wallander,
M.-A., Wilhelmsen, L., & Johansson, S. (2002) <doi:10.1345/aph.1A226>.
Masnoon, N., Shakib, S., Kalisch-Ellett, L., & Caughey, G. E. (2017)
<doi:10.1186/s12877-017-0621-2>. Narayan, S. W., & Nishtala, P. S. (2015)
<doi:10.1007/s40801-015-0020-y>. Nishtala, P. S., & Salahudeen, M. S.
(2015) <doi:10.1159/000368191>. Park, H. Y., Ryu, H. N., Shim, M. K.,
Sohn, H. S., & Kwon, J. W. (2016) <doi:10.5414/cp202484>. Veehof, L.,
Stewart, R., Haaijer-Ruskamp, F., & Jong, B. M. (2000)
<doi:10.1093/fampra/17.3.261>.

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
