%global packname  BDEsize
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Efficient Determination of Sample Size in Balanced Design ofExperiments

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-fpow 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyalert 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-fpow 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyalert 
Requires:         R-CRAN-ggplot2 

%description
Provides the sample size in balanced design of experiments and three
graphs ; detectable standardized effect size vs power, sample size vs
detectable standardized effect size, and sample size vs power. Sample size
is computed in order to detect a certain standardized effect size with
power at the significance level. Three graphs show the mutual relationship
between the sample size, power and the detectable standardized effect
size. By investigating those graphs, it can be checked that which effects
are sensitive to the efficient sample size determination.
Lenth,R.V.(2006-9) <http://www.stat.uiowa.edu/~rlenth/Power> Lim, Yong Bin
(1998) Marvin, A., Kastenbaum, A. and Hoel, D.G. (1970)
<doi:10.2307/2334851> Montgomery, Douglas C. (2013, ISBN: 0849323312).

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
