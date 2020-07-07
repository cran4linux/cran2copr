%global packname  hyper.fit
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          3%{?dist}
Summary:          Generic N-Dimensional Hyperplane Fitting with HeteroscedasticCovariant Errors and Intrinsic Scatter

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.00
Requires:         R-core >= 3.00
BuildArch:        noarch
BuildRequires:    R-CRAN-magicaxis 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-LaplacesDemon 
Requires:         R-CRAN-magicaxis 
Requires:         R-MASS 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-LaplacesDemon 

%description
Includes two main high level codes for hyperplane fitting (hyper.fit) and
visualising (hyper.plot2d / hyper.plot3d). In simple terms this allows the
user to produce robust 1D linear fits for 2D x vs y type data, and robust
2D plane fits to 3D x vs y vs z type data. This hyperplane fitting works
generically for any N-1 hyperplane model being fit to a N dimension
dataset. All fits include intrinsic scatter in the generative model
orthogonal to the hyperplane.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
