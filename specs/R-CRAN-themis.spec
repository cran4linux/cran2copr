%global packname  themis
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          2%{?dist}
Summary:          Extra Recipes Steps for Dealing with Unbalanced Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-recipes >= 0.1.4
BuildRequires:    R-CRAN-dials 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ROSE 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-unbalanced 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-recipes >= 0.1.4
Requires:         R-CRAN-dials 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ROSE 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-unbalanced 
Requires:         R-CRAN-withr 

%description
A dataset with an uneven number of cases in each class is said to be
unbalanced. Many models produce a subpar performance on unbalanced
datasets. A dataset can be balanced by increasing the number of minority
cases using SMOTE 2011 <arXiv:1106.1813>, BorderlineSMOTE 2005
<doi:10.1007/11538059_91> and ADASYN 2008
<https://ieeexplore.ieee.org/document/4633969>. Or by decreasing the
number of majority cases using NearMiss 2003
<https://www.site.uottawa.ca/~nat/Workshop2003/jzhang.pdf> or Tomek link
removal 1976 <https://ieeexplore.ieee.org/document/4309452>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
