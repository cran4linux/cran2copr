%global packname  asnipe
%global packver   1.1.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.13
Release:          1%{?dist}%{?buildtag}
Summary:          Animal Social Network Inference and Permutations for Ecologists

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
Requires:         R-MASS 
Requires:         R-Matrix 

%description
Implements several tools that are used in animal social network analysis,
as described in Whitehead (2007) Analyzing Animal Societies <University of
Chicago Press> and Farine & Whitehead (2015) <doi:
10.1111/1365-2656.12418>. In particular, this package provides the tools
to infer groups and generate networks from observation data, perform
permutation tests on the data, calculate lagged association rates, and
performed multiple regression analysis on social network data.

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
