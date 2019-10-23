%global packname  timeordered
%global packver   0.9.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.9
Release:          1%{?dist}
Summary:          Time-Ordered and Time-Aggregated Network Analyses

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-methods 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-plyr 
Requires:         R-methods 

%description
Approaches for incorporating time into network analysis. Methods include:
construction of time-ordered networks (temporal graphs); shortest-time and
shortest-path-length analyses; resource spread calculations; data
resampling and rarefaction for null model construction; reduction to
time-aggregated networks with variable window sizes; application of common
descriptive statistics to these networks; vector clock latencies; and
plotting functionalities. The package supports
<doi:10.1371/journal.pone.0020298>.

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
