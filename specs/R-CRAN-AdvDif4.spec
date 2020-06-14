%global packname  AdvDif4
%global packver   0.7.18
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.18
Release:          2%{?dist}
Summary:          Solving 1D Advection Bi-Flux Diffusion Equation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
This software solves an Advection Bi-Flux Diffusive Problem using the
Finite Difference Method FDM. Vasconcellos, J.F.V., Marinho, G.M., Zanni,
J.H., 2016, Numerical analysis of an anomalous diffusion with a bimodal
flux distribution. <doi:10.1016/j.rimni.2016.05.001>. Silva, L.G., Knupp,
D.C., Bevilacqua, L., Galeao, A.C.N.R., Silva Neto, A.J., 2014,
Formulation and solution of an Inverse Anomalous Diffusion Problem with
Stochastic Techniques. <doi:10.5902/2179460X13184>. In this version, it is
possible to include a source as a function depending on space and time,
that is, s(x,t).

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
