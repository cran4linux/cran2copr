%global packname  ELMSO
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}
Summary:          Implementation of the Efficient Large-Scale Online DisplayAdvertising Algorithm

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch

%description
An implementation of the algorithm described in "Efficient Large- Scale
Internet Media Selection Optimization for Online Display Advertising" by
Paulson, Luo, and James (Journal of Marketing Research 2018; see URL below
for journal text/citation and
<http://faculty.marshall.usc.edu/gareth-james/Research/ELMSO.pdf> for a
full-text version of the paper). The algorithm here is designed to
allocate budget across a set of online advertising opportunities using a
coordinate-descent approach, but it can be used in any resource-allocation
problem with a matrix of visitation (in the case of the paper, website
page- views) and channels (in the paper, websites). The package contains
allocation functions both in the presence of bidding, when allocation is
dependent on channel-specific cost curves, and when advertising costs are
fixed at each channel.

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
