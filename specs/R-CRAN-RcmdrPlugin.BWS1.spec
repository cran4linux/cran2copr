%global packname  RcmdrPlugin.BWS1
%global packver   0.1-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          R Commander Plug-in for Case 1 (Object Case) Best-Worst Scaling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-support.BWS >= 0.4.1
BuildRequires:    R-CRAN-crossdes 
BuildRequires:    R-CRAN-support.CEs 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-Rcmdr 
Requires:         R-CRAN-support.BWS >= 0.4.1
Requires:         R-CRAN-crossdes 
Requires:         R-CRAN-support.CEs 
Requires:         R-survival 
Requires:         R-CRAN-Rcmdr 

%description
Adds menu items to the R Commander for implementing case 1 (object case)
best-worst scaling (BWS1) from designing choice sets to measuring
preferences for items. BWS1 is a question-based survey method that
constructs various combinations of items (choice sets) using the
experimental designs, asks respondents to select the best and worst items
in each choice set, and then measures preferences for the items by
analyzing the responses. For details on BWS1, refer to Louviere et al.
(2015) <doi:10.1017/CBO9781107337855>.

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
