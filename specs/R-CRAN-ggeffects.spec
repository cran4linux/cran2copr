%global packname  ggeffects
%global packver   0.14.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.14.0
Release:          1%{?dist}
Summary:          Create Tidy Data Frames of Marginal Effects for 'ggplot' fromModel Outputs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-sjmisc >= 2.8.2
BuildRequires:    R-CRAN-sjlabelled >= 1.1.1
BuildRequires:    R-CRAN-insight >= 0.7.1
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
Requires:         R-CRAN-sjmisc >= 2.8.2
Requires:         R-CRAN-sjlabelled >= 1.1.1
Requires:         R-CRAN-insight >= 0.7.1
Requires:         R-graphics 
Requires:         R-CRAN-magrittr 
Requires:         R-MASS 
Requires:         R-CRAN-purrr 
Requires:         R-stats 

%description
Compute marginal effects from statistical models and returns the result as
tidy data frames. These data frames are ready to use with the
'ggplot2'-package. Marginal effects can be calculated for many different
models. Interaction terms, splines and polynomial terms are also
supported. The main functions are ggpredict(), ggemmeans() and ggeffect().
There is a generic plot()-method to plot the results using 'ggplot2'.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
