%global packname  robsurvey
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Survey Statistics Estimation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-survey >= 3.35
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
Requires:         R-CRAN-survey >= 3.35
Requires:         R-grDevices 
Requires:         R-stats 

%description
Multiple functions to compute robust survey statistics. The package
supports the computations of robust means, totals, and ratios. Available
methods are Huber M-estimators, trimming, and winsorization. The package
'robsurvey' complements the 'survey' package. The package additionally
includes a weighted version of the resistant line function of base R
(line()), as well as two median based simple regression estimators. The
methods are described in Hulliger (1995)
<https://www150.statcan.gc.ca/n1/en/catalogue/12-001-X199500114407/>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
