%global __brp_check_rpaths %{nil}
%global packname  rockchalk
%global packver   1.8.144
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.144
Release:          3%{?dist}%{?buildtag}
Summary:          Regression Estimation and Presentation

License:          GPL (>= 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-carData 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-kutils 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-carData 
Requires:         R-MASS 
Requires:         R-CRAN-kutils 

%description
A collection of functions for interpretation and presentation of
regression analysis.  These functions are used to produce the statistics
lectures in <http://pj.freefaculty.org/guides>. Includes regression
diagnostics, regression tables, and plots of interactions and "moderator"
variables. The emphasis is on "mean-centered" and "residual-centered"
predictors. The vignette 'rockchalk' offers a fairly comprehensive
overview.  The vignette 'Rstyle' has advice about coding in R.  The
package title 'rockchalk' refers to our school motto, 'Rock Chalk Jayhawk,
Go K.U.'.

%prep
%setup -q -c -n %{packname}


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
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
