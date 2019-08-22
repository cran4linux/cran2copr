%global packname  BallMapper
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          The Ball Mapper Algorithm

License:          MIT + file LICENCE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-networkD3 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-networkD3 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-fields 
Requires:         R-methods 
Requires:         R-CRAN-stringr 

%description
The core algorithm is described in "Ball mapper: a shape summary for
topological data analysis" by Pawel Dlotko, (2019) <arXiv:1901.07410>.
Please consult the following youtube video
<https://www.youtube.com/watch?v=M9Dm1nl_zSQfor> the idea of
functionality. Ball Mapper provide a topologically accurate summary of a
data in a form of an abstract graph. To create it, please provide the
coordinates of points (in the points array), values of a function of
interest at those points (can be initialized randomly if you do not have
it) and the value epsilon which is the radius of the ball in the Ball
Mapper construction. It can be understood as the minimal resolution on
which we use to create the model of the data.

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
%license %{rlibdir}/%{packname}/LICENCE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
