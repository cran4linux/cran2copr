%global packname  LoopDetectR
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Comprehensive Feedback Loop Detection in ODE Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-numDeriv 

%description
Detect feedback loops (cycles, circuits) between species (nodes) in
ordinary differential equation (ODE) models. Feedback loops are paths from
a node to itself without visiting any other node twice, and they have
important regulatory functions. Loops are reported with their order of
participating nodes and their length, and whether the loop is a positive
or a negative feedback loop. An upper limit of the number of feedback
loops limits runtime (which scales with feedback loop count). Model
parametrizations and values of the modelled variables are accounted for.
Computation uses the characteristics of the Jacobian matrix as described
e.g. in Thomas and Kaufman (2002) <doi:10.1016/s1631-0691(02)01452-x>.
Input can be the Jacobian matrix of the ODE model or the ODE function
definition; in the latter case, the Jacobian matrix is determined using
'numDeriv'. Graph-based algorithms from 'igraph' are employed for path
detection.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
