%global packname  memisc
%global packver   0.99.25.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.99.25.6
Release:          2%{?dist}%{?buildtag}
Summary:          Management of Survey Data and Presentation of Analysis Results

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-lattice 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-MASS 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-repr 
BuildRequires:    R-CRAN-data.table 
Requires:         R-lattice 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-MASS 
Requires:         R-grid 
Requires:         R-CRAN-repr 
Requires:         R-CRAN-data.table 

%description
An infrastructure for the management of survey data including value
labels, definable missing values, recoding of variables, production of
code books, and import of (subsets of) 'SPSS' and 'Stata' files is
provided. Further, the package allows to produce tables and data frames of
arbitrary descriptive statistics and (almost) publication-ready tables of
regression model estimates, which can be exported to 'LaTeX' and HTML.

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
