%global packname  AR
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Another Look at the Acceptance-Rejection Method

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-DISTRIB 
Requires:         R-CRAN-DISTRIB 

%description
In mathematics, 'rejection sampling' is a basic technique used to generate
observations from a distribution. It is also commonly called 'the
Acceptance-Rejection method' or 'Accept-Reject algorithm' and is a type of
Monte Carlo method. 'Acceptance-Rejection method' is based on the
observation that to sample a random variable one can perform a uniformly
random sampling of the 2D cartesian graph, and keep the samples in the
region under the graph of its density function. Package 'AR' is able to
generate/simulate random data from a probability density function by
Acceptance-Rejection method. Moreover, this package is a useful teaching
resource for graphical presentation of Acceptance-Rejection method. From
the practical point of view, the user needs to calculate a constant in
Acceptance-Rejection method, which package 'AR' is able to compute this
constant by optimization tools. Several numerical examples are provided to
illustrate the graphical presentation for the Acceptance-Rejection Method.

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
