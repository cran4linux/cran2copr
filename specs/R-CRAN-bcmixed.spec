%global __brp_check_rpaths %{nil}
%global packname  bcmixed
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          3%{?dist}%{?buildtag}
Summary:          Mixed Effect Model with the Box-Cox Transformation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.3
Requires:         R-core >= 3.3.3
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.45
BuildRequires:    R-nlme >= 3.1.131
Requires:         R-MASS >= 7.3.45
Requires:         R-nlme >= 3.1.131

%description
Inference on the marginal model of the mixed effect model with the Box-Cox
transformation and on the model median differences between treatment
groups for longitudinal randomized clinical trials. These statistical
methods are proposed by Maruo et al. (2017) <doi:10.1002/sim.7279>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
