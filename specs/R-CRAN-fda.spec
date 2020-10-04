%global packname  fda
%global packver   5.1.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.1.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Functional Data Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-Matrix 
Requires:         R-Matrix 

%description
These functions were developed to support functional data analysis as
described in Ramsay, J. O. and Silverman, B. W. (2005) Functional Data
Analysis. New York: Springer and in Ramsay, J. O., Hooker, Giles, and
Graves, Spencer (2009). Functional Data Analysis with R and Matlab
(Springer). The package includes data sets and script files working many
examples including all but one of the 76 figures in this latter book.
Matlab versions are available by ftp from
<http://www.psych.mcgill.ca/misc/fda/downloads/FDAfuns/>.

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
