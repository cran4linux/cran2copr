%global __brp_check_rpaths %{nil}
%global packname  nomogramFormula
%global packver   1.2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Calculate Total Points and Probabilities for Nomogram

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-do 
BuildRequires:    R-CRAN-Hmisc 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-do 
Requires:         R-CRAN-Hmisc 

%description
A nomogram, which can be carried out in 'rms' package, provides a
graphical explanation of a prediction process. However, it is not very
easy to draw straight lines, read points and probabilities accurately.
Even, it is hard for users to calculate total points and probabilities for
all subjects. This package provides formula_rd() and formula_lp()
functions to fit the formula of total points with raw data and linear
predictors respectively by polynomial regression. Function points_cal()
will help you calculate the total points. prob_cal() can be used to
calculate the probabilities after lrm(), cph() or psm() regression. For
more complex condition, interaction or restricted cubic spine,
TotalPoints.rms() can be used.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
