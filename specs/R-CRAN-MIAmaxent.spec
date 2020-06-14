%global packname  MIAmaxent
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          2%{?dist}
Summary:          A Modular, Integrated Approach to Maximum Entropy DistributionModeling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-raster >= 2.5.8
BuildRequires:    R-CRAN-e1071 >= 1.6.7
BuildRequires:    R-CRAN-dplyr >= 0.4.3
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-raster >= 2.5.8
Requires:         R-CRAN-e1071 >= 1.6.7
Requires:         R-CRAN-dplyr >= 0.4.3
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Tools for training, selecting, and evaluating maximum entropy (and
standard logistic regression) distribution models. This package provides
tools for user-controlled transformation of explanatory variables,
selection of variables by nested model comparison, and flexible model
evaluation and projection. It follows principles based on the maximum-
likelihood interpretation of maximum entropy modeling, and uses
infinitely- weighted logistic regression for model fitting.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
