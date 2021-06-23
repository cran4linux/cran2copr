%global __brp_check_rpaths %{nil}
%global packname  regclass
%global packver   1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6
Release:          3%{?dist}%{?buildtag}
Summary:          Tools for an Introductory Class in Regression and Modeling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-bestglm 
BuildRequires:    R-CRAN-leaps 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-rpart.plot 
Requires:         R-CRAN-bestglm 
Requires:         R-CRAN-leaps 
Requires:         R-CRAN-VGAM 
Requires:         R-rpart 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-rpart.plot 

%description
Contains basic tools for visualizing, interpreting, and building
regression models.  It has been designed for use with the book
Introduction to Regression and Modeling with R by Adam Petrie, Cognella
Publishers, ISBN: 978-1-63189-250-9
<https://titles.cognella.com/introduction-to-regression-and-modeling-with-r-9781631892509>.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
