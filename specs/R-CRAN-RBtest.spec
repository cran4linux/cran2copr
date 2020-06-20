%global packname  RBtest
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Regression-Based Approach for Testing the Type of Missing Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-psych 
Requires:         R-nnet 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-psych 

%description
The regression-based (RB) approach is a method to test the missing data
mechanism. This package contains two functions that test the type of
missing data (Missing Completely At Random vs Missing At Random) on the
basis of the RB approach. The first function applies the RB approach
independently on each variable with missing data, using the completely
observed variables only. The second function tests the missing data
mechanism globally (on all variables with missing data) with the use of
all available information. The algorithm is adapted both to continuous and
categorical data.

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

%files
%{rlibdir}/%{packname}
