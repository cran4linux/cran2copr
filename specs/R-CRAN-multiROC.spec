%global packname  multiROC
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          3%{?dist}
Summary:          Calculating and Visualizing ROC and PR Curves Across Multi-ClassClassifications

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-boot 
BuildRequires:    R-stats 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-magrittr 
Requires:         R-boot 
Requires:         R-stats 

%description
Tools to solve real-world problems with multiple classes classifications
by computing the areas under ROC and PR curve via micro-averaging and
macro-averaging. The vignettes of this package can be found via
<https://github.com/WandeRum/multiROC>. The methodology is described in V.
Van Asch (2013)
<https://www.clips.uantwerpen.be/~vincent/pdf/microaverage.pdf> and
Pedregosa et al. (2011)
<http://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html>.

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
