%global __brp_check_rpaths %{nil}
%global packname  QCAcluster
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for the Analysis of Clustered Data in QCA

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-QCA >= 3.7
BuildRequires:    R-CRAN-plyr >= 1.8.5
BuildRequires:    R-CRAN-stringi >= 1.7.4
BuildRequires:    R-CRAN-UpSetR >= 1.4.0
BuildRequires:    R-CRAN-data.table >= 1.12.8
BuildRequires:    R-CRAN-rlist >= 0.4.6.1
BuildRequires:    R-CRAN-purrr >= 0.3.3
BuildRequires:    R-CRAN-testit >= 0.11
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-QCA >= 3.7
Requires:         R-CRAN-plyr >= 1.8.5
Requires:         R-CRAN-stringi >= 1.7.4
Requires:         R-CRAN-UpSetR >= 1.4.0
Requires:         R-CRAN-data.table >= 1.12.8
Requires:         R-CRAN-rlist >= 0.4.6.1
Requires:         R-CRAN-purrr >= 0.3.3
Requires:         R-CRAN-testit >= 0.11
Requires:         R-CRAN-magrittr 

%description
Clustered set-relational data in Qualitative Comparative Analysis (QCA)
can have a hierarchical structure, a panel structure or repeated cross
sections. 'QCAcluster' allows QCA researchers to supplement the analysis
of pooled the data with a disaggregated perspective focusing on selected
partitions of the data. The pooled data can be partitioned along the
dimensions of the clustered data (individual cross sections or time
series) to perform partition-specific truth table minimizations. Empirical
researchers can further calculate the weight that each partition has on
the parameters of the pooled solution and the diversity of the cases under
analysis within and across partitions (see
<https://ingorohlfing.github.io/QCAcluster/>).

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
