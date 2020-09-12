%global packname  ivitr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate IV-Optimal Individualized Treatment Rules

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-nnet 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 

%description
A method that estimates an IV-optimal individualized treatment rule. An
individualized treatment rule is said to be IV-optimal if it minimizes the
maximum risk with respect to the putative IV and the set of IV
identification assumptions. Please refer to <arXiv:2002.02579> for more
details on the methodology and some theory underpinning the method.
Function IV-PILE() uses functions in the package 'locClass'. Package
'locClass' can be accessed and installed from the 'R-Forge' repository via
the following link: <https://r-forge.r-project.org/projects/locclass/>.
Alternatively, one can install the package by entering the following in R:
'install.packages("locClass", repos="<http://R-Forge.R-project.org>")'.

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
