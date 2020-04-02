%global packname  Rprofet
%global packver   2.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.1
Release:          1%{?dist}
Summary:          WOE Transformation and Scorecard Builder

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-binr 
BuildRequires:    R-CRAN-ClustOfVar 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-sqldf 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-binr 
Requires:         R-CRAN-ClustOfVar 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-sqldf 
Requires:         R-CRAN-stringr 

%description
Performs all steps in the credit scoring process. This package allows the
user to follow all the necessary steps for building an effective
scorecard. It provides the user functions for coarse binning of variables,
Weights of Evidence (WOE) transformation, variable clustering, custom
binning, visualization, and scaling of logistic regression coefficients.
The results will generate a scorecard that can be used as an effective
credit scoring tool to evaluate risk. For complete details on the credit
scoring process, see Siddiqi (2005, ISBN:047175451X).

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
