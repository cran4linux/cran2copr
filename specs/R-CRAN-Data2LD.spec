%global __brp_check_rpaths %{nil}
%global packname  Data2LD
%global packver   3.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Functional Data Analysis with Linear Differential Equations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-splines 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rmarkdown 
Requires:         R-CRAN-fda 
Requires:         R-splines 
Requires:         R-graphics 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rmarkdown 

%description
Provides methods for using differential equations as modelling objects as
described in J. Ramsay G. and Hooker (2017,ISBN 978-1-4939-7188-6) Dynamic
Data Analysis, New York: Springer. Data sets and script files for
analyzing many of the examples in this book are included. This version
corrects bugs and adds two new demos, CruiseControl and
monotoneSmoothDemo. This version incorporates a new system for indexing
coefficient list objects. The step of setting up a set of coefficient list
objects has been eliminated and the functions make.Coef() and coefCheck
have been dropped. 'Matlab' versions of the code and sample analyses are
available by ftp from the website.  There you find a set of .zip files
containing the functions and sample analyses, as well as two .txt files
giving instructions for installation and some additional information.

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
