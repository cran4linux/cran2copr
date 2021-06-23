%global __brp_check_rpaths %{nil}
%global packname  WeibullFit
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Fits and Plots a Dataset to the Weibull Probability DistributionFunction

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-sqldf 
BuildRequires:    R-CRAN-R.oo 
BuildRequires:    R-CRAN-FAdist 
BuildRequires:    R-CRAN-mixdist 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-kSamples 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-R.methodsS3 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-sqldf 
Requires:         R-CRAN-R.oo 
Requires:         R-CRAN-FAdist 
Requires:         R-CRAN-mixdist 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-kSamples 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-R.methodsS3 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides a single function to fit data of an input data frame into one of
the selected Weibull functions (w2, w3 and it's truncated versions),
calculating the scale, location and shape parameters accordingly. The
resulting plots and files are saved into the 'folder' parameter provided
by the user. References: a) John C. Nash, Ravi Varadhan (2011). "Unifying
Optimization Algorithms to Aid Software System Users: optimx for R"
<doi:10.18637/jss.v043.i09>.

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
%{rlibdir}/%{packname}/INDEX
