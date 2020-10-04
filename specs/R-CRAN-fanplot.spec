%global packname  fanplot
%global packver   3.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.4.2
Release:          3%{?dist}%{?buildtag}
Summary:          Visualisation of Sequential Probability Distributions Using FanCharts

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-methods 
Requires:         R-methods 

%description
Visualise sequential distributions using a range of plotting styles.
Sequential distribution data can be input as either simulations or values
corresponding to percentiles over time. Plots are added to existing
graphic devices using the fan function. Users can choose from four
different styles, including fan chart type plots, where a set of coloured
polygon, with shadings corresponding to the percentile values are layered
to represent different uncertainty levels. Full details in R Journal
article; Abel (2015) <doi:10.32614/RJ-2015-002>.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/model
%doc %{rlibdir}/%{packname}/netelicit
%{rlibdir}/%{packname}/INDEX
