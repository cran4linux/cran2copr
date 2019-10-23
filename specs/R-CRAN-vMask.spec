%global packname  vMask
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Detect Small Changes in Process Mean using CUSUM Control Chartby v-Mask

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
The cumulative sum (CUSUM) control chart is considered to be an
alternative or complementary to Shewhart control charts in statistical
process control (SPC) applications, owing to its higher sensitivity to
small shifts in the process mean. It utilizes all the available data
rather than the last few ones used in Shewhart control charts for quick
decision making. V-mask is a traditional technique for separating
meaningful data from unusual circumstances in a Cumulative Sum (CUSUM)
control chart; for see details about v-mask see Montgomery (1985,
ISBN:978-0471656319). The mask is a V-shaped overlay placed on the CUSUM
chart so that one arm of the V lines up with the slope of data points,
making it easy to see data points that lie outside the slope and to
determine whether these points should be discarded as random events, or
treated as a performance trend that should be addressed. But, complex
computations is one disadvantage V-mask method for detect small changes in
mean using CUSUM control chart. Package 'vMask' can help to the applied
users to overcome this challenge by considering six different methods
which each of them are based on different information.

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
